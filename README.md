#  MacroAnvilDupe (MAD)
Well, since [Glorman](https://github.com/GGlorman/AnvilDupe) did a Anvil duper and called it a "Auto" Anvil Duper i decided to fork it and do a high ping version so yeah, if you are a high ping player on 1F2D and want to have a "Auto" duper here it is.\
\
I put quotes on his "Auto" thing cuz its more like a macro and not a smart bot, i don't judge him.\
Forked and modified by Visivel :3
## How it works?

`Clone and download the repository to your computer.`\
`Extract it wherever you want.`\
`Open a Command Prompt and put the directory to where you downloaded.`\
`Do py main.py`\
`In Minecraft open the Anvil Gui and click on the item that you wish to dupe.`\
`Press ] and it will rename it with a space.`\
`Press ] until the anvil breaks.`

## Dependencies and Installation for dummies

Since Glorman didn't told you about Dependencies here is it in case if the duper doesn't works:

You will need to install this stuff (using cmd) on where you downloaded the duper

```bash
  py -m pip install pyautogui
  py -m pip install pynput
```
Btw you will need Pip installed on your computer to execute it on your cmd
    
## Features!

- Slower duper adapted for ~250ms players
- Changed the keybind to ] instead of L


## Known bugs

- Screen size: 
Depending of your monitor, the macro can go outside of the anvil
- Delay: 
If your ping is higher than 250ms you will have to slow down the duper (maybe can work with 350ms)

HOW DO I FIX IT?!?!? Fix by yourself changing the code, isn't that hard.\
You just gotta to change `pyautogui.moveTo(spot of the anvil)` and `sleep(delay)`

  
