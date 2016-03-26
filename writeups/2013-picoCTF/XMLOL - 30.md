#XMLOL: 30
The book has instructions on how to dump the corrupted configuration file from the robot's memory. You find a corrupted XML file and are looking for a configuration key.

##Answer
So we simply open the XML in our web browser, right click and view source.

This gives us the source of the broken XML

```
<?xml version="1.0" encoding="UTF-8" ?>
<garbage
  <writing>
    <?xml verion="1.0" encoding"UTF-8"
      is really

    <super_secret_flag>421259173230972467344526324586</super_secret_flag>

</ gar <bage>
```

And the answer is... `421259173230972467344526324586`
