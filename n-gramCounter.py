from collections import defaultdict
import string 

def count_ngrams(file_name, n=2): 
    #reads in string
    file_string = ""
    with open(file_name, 'r') as f:
        for line in f:
            file_string = file_string + line
            
    #reformatting file_string to remove punctuation
    file_string = file_string.replace("\n"," ").replace("\r", "")
    file_string = file_string.translate(str.maketrans('', '', string.punctuation))
    file_string = file_string.lower()

    #makes n_gram_dict
    n_gram_dict = defaultdict(int)
    #all values in n_gram_dict starts as 0
    ind_word_arr = file_string.split(" ")
    for ind in range((len(ind_word_arr)-(n-1))-1):
        n_gram = ()
        for i in range(ind,ind+n):
            #appends to the n_gram tuple
            n_gram = n_gram + (ind_word_arr[i],)
        #if the n_gram is already in the dictionary, increase count
        if(n_gram in n_gram_dict):
            n_gram_dict[n_gram] = n_gram_dict[n_gram] +1
        #if the n_gram is not in the dictionary yet, give it count one
        else:
            n_gram_dict[n_gram] = 1
    return n_gram_dict


def single_occurences(ngram_count_dict): 
    single_occurance_list = []
    #iterates over dict
    for key, value in ngram_count_dict.items():
        #if the count value in the dictionary is one, add it to list
        if(value==1):
            single_occurance_list.append(key)
    return single_occurance_list

def most_frequent(ngram_count_dict, num): 
    freq_list = []
    #iterates over dict
    for key, value in ngram_count_dict.items():
        #append value, key tuple to list
        freq_list.append((value, key))
    #sorts list from smallest to greastest count
    freq_list.sort(key=lambda tup: tup[0])
    nmost_frequented_list = []
    #reverses order from greatest to smallest count
    freq_list = freq_list[::-1]
    for i in range(num):
        #appends the n-gram to the most frequented list
        nmost_frequented_list.append(freq_list[i][1])
    return nmost_frequented_list

def main():
    filename = "alice.txt"
    n = 3
    most_frequent_k = 5

    ngram_counts = count_ngrams(filename, n)

    print('{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))

    print('{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))

if __name__ == "__main__":
    main()
