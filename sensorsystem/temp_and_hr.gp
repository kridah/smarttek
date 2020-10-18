# Separate values by comma
set datafile separator ","

# Output to PDF
set terminal pngcairo size 1280,720 font "Helvetica" background rgb 'white'
set output "temp_and_hr.png"

# Auto generate stats for the 'data.csv' file to use later
stats "readings.csv" using 1:2 name "stats"

# Function returning how many data points we have processed (and should divide by to get average).
# Capped to at least 1 and max 5.
samples(x) = $0 > 4 ? 5 : ($0+1)

# Function to put current data point in back1, previous back1 value into back2, etc. ...
shift5(x) = (back5 = back4, back4 = back3, back3 = back2, back2 = back1, back1 = x)

# Function that calls shift above, then calculate average of all backX values (last 1-5 data points).
avg5(x) = (shift5(x), (back1+back2+back3+back4+back5)/samples($0))

# Function to initialise values to 0 at start.
init(x) = (back1 = back2 = back3 = back4 = back5 = sum = 0)

set xlabel "Tid (sekunder)"

set multiplot layout 3,1 title "Temperatur og fotopletysmograf"

set title "Temperatur"
plot 'readings.csv' using 1:3 lt 5 lc 4 notitle

unset key
unset y2tics
set title "Rådata - hr"
set yrange[170:179]
plot 'readings.csv' using 1:2 lt 7 lc 2 w l,
# Actual plot (Note: Using stats, not the data file!)
set title "5-punkt gjennomsnitt - hr"
plot sum = init(0), \
     '' using ($1-stats_min_x):(avg5($2)) with lines smooth csplines lc rgb '#aa7777' notitle ''
unset multiplot