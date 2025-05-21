# specification

this is a 2D esolang. the program pointer starts in the upper left corner (0, 0)

## memory
there are 2 methods used to store values, the stack and the line array.

### stack
the stack is arbitrarily long. you can only push and pop to the stack.
the stack is used for most instruction arguments.

### line array
the `,` instruction stores the value on the top of the stack to an array indexed
by the line number. The line array can be indexed and retrieved from using the `=`
instruction.

## instructions
| instruction | purpose                                                         |
|-------------|-----------------------------------------------------------------|
| q           | ends the program                                                |
| _           | gets user input and puts it on the stack                        |
| :           | pushes next value to top of stack as a string                   |
| d           | duplicate top of stack                                          |
| /           | pops from the stack                                             |
| +           | adds top 2 values on stack                                      |
| *           | multiply top 2 numbers on stack                                 |
| -           | negates number on top of stack                                  |
| &           | get inverse of number on top of stack                           |
| .           | prints value on top of stack                                    |
| ,           | store top of stack into the line array indexed with line number |
| =           | gets value from the line array in top of stack                  | 
| i           | converts value on top of stack to int                           |
| a           | convert letter to utf value                                     | 
| v           | move pointer down one line                                      |
| V           | move pointer down a line and go to start of line                |
| k           | move pointer up                                                 |
| K           | move pointer up and to start of line                            |
| j           | jump to a line (keeps index)                                    |
| J           | jump to a line (goes to index 0)                                |
| x           | if top of stack is 0, move down a line                          |
| c           | call to line number from stack                                  |
| r           | return from call                                                |
| \>          | enter feed mode                                                 |

## feed mode

### step mode
steps over character unless it is a feed instruction

### load mode
when entering load mode an empty string is places on top of the stack

in load mode, any characters other than `:` are added to the top of the stack

when it encounters another `:` load mode is exited back in to step mode

### feed instructions
| instruction | purpose                                                |
|-------------|--------------------------------------------------------|
| s           | step, does nothing with information (ignores commands) |
| :           | load string into stack until another : is reached      |
| \|          | exit feed mode                                         |

# examples

## hello world
```
>:hello, world!:|.q
```

## truth-machine
```
_ix:1i-+xq  V
> .q|   :1./k
```

## fibonacci sequence up to n=10
```
  v
,rv
,r:1i,/v
,r     v
,r     >:10:|i,V
:1=:2=+:3c//V
:2=:1c/:3=:2c .V
:4=:1i-+:4cxV
/:5J       q
```

## four function calculator
```
_i_iV
_a:+a-+x:+a+:-a-+x:-a+:*a-+x:*a+:/a-+xV
V      /+.q      /-+.q     /*.q      /&*.q
>:unrecognized operation:|.q
```