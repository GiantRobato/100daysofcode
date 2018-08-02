from __future__ import print_function

import collections

#python default hash function
#number of collisions around 4000, changes each time due to python's randomization of the hash function
def hashFunction(word):
    return hash(word)

#java's hascode uses 31 src: https://docs.oracle.com/javase/1.5.0/docs/api/java/lang/String.html#hashCode%28%29
#numCollisions: 4295
def hashFunction1(word):
    hashCode = 0
    n = len(word)
    for i,letter in enumerate(word):
        hashCode += ord(letter) * (31 ** (n - i - 1))
    return hashCode

#java's hashcode but using 92821 per this SO post: https://stackoverflow.com/questions/1835976/what-is-a-sensible-prime-for-hashcode-calculation/2816747#2816747
#numCollisions: 4098
def hashFunction2(word):
    hashCode = 0
    n = len(word)
    for i,letter in enumerate(word):
        hashCode += ord(letter) * (92821 ** (n - i - 1))
    return hashCode

#using FNV-1a 32 bit version more info: http://isthe.com/chongo/tech/comp/fnv/
#numCollisions 4120
def hashFunction3(word):
    #start with a basis, can add seed for randomization 
    hashCode = 2166136261
    FNV_prime = 16777619
    for letter in word:
        hashCode = hashCode ^ ord(letter)
        hashCode = hashCode * FNV_prime
    return hashCode    

#using FNV-1a 64 bit version more info: http://isthe.com/chongo/tech/comp/fnv/
#numCollisions 4089
def hashFunction4(word):
    #start with a basis, can add seed for randomization 
    hashCode = 14695981039346656037
    FNV_prime = 1099511628211
    for letter in word:
        hashCode = hashCode ^ ord(letter)
        hashCode = hashCode * FNV_prime
    return hashCode 

#using stupid simple hashfunction
#numCollisions 18,837
def hashFunction5(word):
    hashCode = 0
    for letter in word:
        hashCode += ord(letter)
    return hashCode 

class HashSet:
    """
    Simple hashset
    """

    def __init__(self):
        self.size = 10
        self.count = 0
        self.arr = [[] for _ in range(self.size)]
        self.loadFactor = 0.7
    
    def add(self,word):
        """
        Adds word to hashSet, if 
        """
        self.count += 1
        if float(self.count) / float(self.size) > self.loadFactor:
            self.resize()
        idx = hashFunction(word) % self.size
        self.arr[idx].append(word)        

    def resize(self):
        """
        reached load factor of hash table, double hash table size and for each word, copy over
        """
        self.size = self.size * 2
        newArr = [[] for _ in range(self.size)]
        for bucket in self.arr:
            if not bucket: continue #skip empty buckets
            for word in bucket:
                hashCode = hashFunction(word)
                newidx = hashCode % self.size
                newArr[newidx].append(word)
        self.arr = newArr            
    
    def count_collisions(self):
        """
        goes through our hash set and checks if there was a collision,
        if so, add the number of collisions at that bucket
        """
        count = 0
        for bucket in self.arr:
            if bucket and len(bucket) > 1: count += len(bucket) - 1
        return count

    def load_factor(self):
        """
        calculates our load amount which is how many values we've stored over our capacity
        """
        return float(self.count) / float(self.size)

hashSet = HashSet()

with open('words.txt','r') as f:
    line = f.readline().strip()
    while line:
        hashSet.add(line)
        line = f.readline().strip()

print('size of hashtable: {}'.format(hashSet.size))
print('num collisions: {}'.format(hashSet.count_collisions()))