#!/bin/bash


################

trap 'echo "trap: signal ignored"'  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
disown


if [ "x$HTTP_X_FORWARDED_FOR" != x ]
then    # via proxy
        REMOTE_ADDR="$HTTP_X_FORWARDED_FOR"
fi

echo 'Content-type: text/plain
'


QUERY_STRING="$QUERY_STRING&$(cat)"     # html-get+post
eval $(echo "$QUERY_STRING"| tr -s '&' '\012'|egrep "info")


case "$info_cmd" in
show)   
    /opt/nts/bin/get_config -h $info_host --detail
    ;;
*)
    echo "wrong cmd \"$info_cmd\""
    ;;
esac




