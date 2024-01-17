from typing import List

def removeDupl(elements: List) -> List:
    sol = []
    for elem in elements:
        if elem in sol:
            continue
        sol.append(elem)
    
    return sol

def main():
    test = [1,2,2,3]
    print(removeDupl(test))

if __name__ == "__main__":
    main()