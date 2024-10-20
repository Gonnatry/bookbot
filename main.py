path_to_file = "books/frankenstein.txt"

def sort_by_num(item):
    return item['num']

def Count(book):
    word_count = book.split()
    return len(word_count)

def Count_Character(book):
    lower_book = book.lower()
    word_list = lower_book.split()
    
    character_dict = {}

    for word in word_list:
        for w in word:
            if w not in character_dict:
                character_dict[w] = 1
            else:
                character_dict[w] +=1
    return character_dict

def Sort_Data(count_dict):
    alpha_list = []
    #print(count_dict)

    for count in count_dict:
        #print(count)
        if count.isalpha():
            tmp_dict = {"character":count, "num":count_dict[count]}

            alpha_list.append(tmp_dict)
        
    alpha_list.sort(reverse=True, key=sort_by_num)

    return alpha_list 

def Create_Report(book):
    word_count = Count(book)
    character_dict = Count_Character(book)
    sorted_dict_list = Sort_Data(character_dict) 

    print("--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print()
    print()

    for sorted in sorted_dict_list:
        print(f"The '{sorted["character"]}' character was found {sorted["num"]} times")
    print("--- End report ---")


def main():
    
    with open(path_to_file) as f:
        file_contents = f.read()

    Create_Report(file_contents)
    


    #print (file_contents)


main()