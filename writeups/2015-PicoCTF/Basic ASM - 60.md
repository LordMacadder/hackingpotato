#Basic ASM - 60
We found this program snippet.txt, but we're having some trouble figuring it out. What's the value of %eax when the last instruction (the NOP) runs?

##Solution
1. Turn the A&T code into pseudo code

   ```
   # This file is in AT&T syntax - see http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
   # and http://en.wikipedia.org/wiki/X86_assembly_language#Syntax. Both gdb and objdump produce
   # AT&T syntax by default.
   MOV $23133,%ebx   # Move 23133 to ebx
   MOV $12733,%eax   # Move 12733 to eax
   MOV $27798,%ecx   # Move 27798 to ecx
   CMP %eax,%ebx     # if eax (12733) is equal to ebx (23133) then jump to L1, else jump to L2
   JL L1             # Ignore this above wasn't true
   JMP L2            # Jump to L2
   L1:
     IMUL %eax,%ebx  # multiply eax and ebx, save to ebx
     ADD %eax,%ebx   # add eax to ebx
     MOV %ebx,%eax   # Move ebx to eax
     SUB %ecx,%eax   # Subtract ecx from eax
     JMP L3
   L2:
     IMUL %eax,%ebx  # multiply eax and ebx, save to ebx - 294552489
     SUB %eax,%ebx   # subtract eax from ebx, save to ebx - 294539756
     MOV %ebx,%eax   # Move ebx to eax, save to eax - 294539756
     ADD %ecx,%eax   # add ecx to eax, save to eax - 294567554
   L3:
     NOP             # The value of eax is - 294567554
   ```
