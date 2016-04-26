#avaJ: 85
elif avaJ

## Solution
1. After decompiling using [java decompiler]() we can see lots of sequences that look like

   ```
    if (string.length() != 16) {
        System.out.println("Wrong");
        return;
    }
    char[] arrc = string.toCharArray();
    if (arrc[0] != 'i') {
        System.out.println("Wrong");
        return;
    }
    if (arrc[1] != 'T') {
        System.out.println("Wrong");
        return;
    }
   ```

2. We also see a set of lines that reads 

   ```
   System.out.print("Correct, your key is: ");
   System.out.println(string);
   ```

3. So we can deduce the key is the password, so we set about simply writing out the letters from step 1, to read `iT6chiweTohy4oot`

