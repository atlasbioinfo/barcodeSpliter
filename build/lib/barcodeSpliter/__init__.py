def main():
    from sys import version_info
    if version_info.major != 3:
        print("Warning!")
        print('\tYour python version is '+str(version_info.major)+'.'+str(version_info.minor))
        print('\t"Please use python3 (Recommended python>=3.6.0)!')
        print('barcodeSpliter exit...')
        return
    from barcodeSpliter.barcodeSpliter import main
    main()


if __name__ == "__main__":
    main()