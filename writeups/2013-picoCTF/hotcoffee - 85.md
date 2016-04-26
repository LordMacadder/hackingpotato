#hotcoffee: 85
This is a compiled Java class file. It looks like it will accept a password, but only one. Can you find the password and control the planet?

Download the class file here or look on the shell machine in /problems/hotcoffee/

## Solution
1. Upload the class to my favourite [online decompiler](http://www.javadecompilers.com/)

2. Analysing the code we can see

   ```
    String string = scanner.next();
    if (string.equals("eupai1AhNu7aeTho")) {
        System.out.println("Correct");
        System.out.print("Your key is: ");
        System.out.print("n");
        System.out.print("0");
        System.out.print("t");
        System.out.print("h");
        System.out.print("1");
        System.out.print("n");
        System.out.print("g");
        System.out.print("_");
        System.out.print("1");
        System.out.print("s");
        System.out.print("_");
        System.out.print("s");
        System.out.print("a");
        System.out.print("f");
        System.out.print("3");
        System.out.print("\n");
    } else {
        System.out.println("Wrong");
    }
   ```

3. We can see key being printed out letter by letter after the password check `n0th1ng_1s_saf3`
