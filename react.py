import os

def check_if_component_direct_exist():
    if not os.path.exists('components'):
        os.makedirs('components')

def main():
    check_if_component_direct_exist()

if __name__ == "__main__":
    main()
