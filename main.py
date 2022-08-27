import colorama, pyttsx3, basic_1, internet_1, silly
foreground = colorama.Fore
tts = pyttsx3.init()


def breakdown(text):
    print(foreground.LIGHTYELLOW_EX + "Debug: Breaking Down Input")
    text = text.split()
    # print(foreground.LIGHTGREEN_EX + "Debug #0:", text)  # DEBUG
    commands = open("commands/commands.txt", "r")
    likeness = {}
    for line in commands:
        count = 0
        line = line.split(":")
        fun = str(line[0])
        line[1].strip("\n")
        line[1] = line[1].split()
        # print(foreground.LIGHTGREEN_EX + "Debug #1:", line)  # DEBUG
        for part in line[1]:
            for word in text:
                if word == part:
                    count += 1
        likeness[str(fun)] = count # not appending to dict
        # print(foreground.LIGHTGREEN_EX + "Debug #2:", likeness)  # DEBUG
    print(foreground.LIGHTGREEN_EX + "Likeness:", likeness)  # DEBUG

    # Finding most likely command
    print(foreground.LIGHTYELLOW_EX + "Finding most like")
    top = 0
    num = ""
    for key in likeness:
        if likeness[key] > top:
            top = likeness[key]
            num = key
    print(foreground.LIGHTGREEN_EX + "Debug #3:", top)
    print(foreground.LIGHTGREEN_EX + "Debug #3:", num)
    return num


def execute(num):
    print(foreground.LIGHTYELLOW_EX + "Debug: Code Executing")
    command_file = open("commands/functions.txt", "r")
    for line in command_file:
        if int(line[0]) == int(num):
            command = line
            break
        else:
            command = ""
    if command != "":
        cut = str(num + ":")
        command = command.strip(cut)
    print(foreground.LIGHTGREEN_EX + "Debug #4:", command)
    # execute!
    exec(command)


def cmd():
    entry = str(input(" >> "))
    if entry == "quit":
        quit("goodbye")
    else:
        print(foreground.CYAN + "User:", entry)  # USER
        comm = breakdown(entry)
        execute(comm)


def main():
    while True:
        cmd()


main()
