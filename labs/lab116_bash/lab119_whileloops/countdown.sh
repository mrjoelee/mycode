COUNTER=$1
COUNTER=$(( COUNTER * 5 ))

minusone(){
        COUNTER=$(( COUNTER - 1 ))
        sleep 1
}

while [ $COUNTER -gt 0 ]
do
        echo "You have $COUNTER seconds left!"
        minusone
done

[ $COUNTER = 0 ] && echo "Time is up." && minusone
[ $COUNTER = "-1" ] && echo "You are late!" && minusone

while true
do
        echo "You are now ${COUNTER#-} seconds late!"
        minusone
done

