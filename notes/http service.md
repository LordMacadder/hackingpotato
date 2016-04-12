#HTTP Service

## To start
run `service apache2 start`

## To verify
Navigate to your localhost in a browser `http://127.0.0.1`

## Document root
The document root for apache can be found in `/var/www` this can be tested by replacing the index

```
root@kali:/# echo "john rocks" > /var/www/index.html
```

## To Stop
run `service apache2 stop`
