def main():
    command = "REPEAT 3 TIMES: PRINT Hello"

    # Split the command into words based on whitespace
    words = command.split(" ")

    # Handle the command
    if words[0].upper() == "REPEAT":
        repeat_count = int(words[1])
        for i in range(repeat_count):
            if words[3].upper() == "PRINT":
                print(words[4])

    # 很明顯這種方式非常不容易拓展，
    # 如果需要增添新命令就需要修改代碼邏輯，
    # 可以看得出來這將會是一場惡夢，
    # 並且會有非常低的可維護性。

if __name__ == "__main__":
    main()
