#include <stdlib.h>
#include <stdio.h>

// Node structure for separate chaining
typedef struct HashNode {
    int key;
    int value;
    struct HashNode* next;
} HashNode;

// Simple hash table structure
typedef struct {
    HashNode** buckets;
    int size;
} HashTable;

// Hash function to get an index
int hash(int key, int size) {
    return abs(key) % size;
}

// Initialize the hash table with given size
HashTable* createHashTable(int size) {
    HashTable* table = (HashTable*)malloc(sizeof(HashTable));
    table->buckets = (HashNode**)calloc(size, sizeof(HashNode*));
    table->size = size;
    return table;
}

// Insert key-value pair into the hash table using separate chaining
void insert(HashTable* table, int key, int value) {
    int index = hash(key, table->size);
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->value = value;
    newNode->next = table->buckets[index];
    table->buckets[index] = newNode;
}

// Find value by key in the hash table
int find(HashTable* table, int key, int* found) {
    int index = hash(key, table->size);
    HashNode* current = table->buckets[index];
    while (current != NULL) {
        if (current->key == key) {
            *found = 1;
            return current->value;
        }
        current = current->next;
    }
    *found = 0;
    return -1;
}

// Free the hash table
void freeHashTable(HashTable* table) {
    for (int i = 0; i < table->size; i++) {
        HashNode* current = table->buckets[i];
        while (current != NULL) {
            HashNode* temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(table->buckets);
    free(table);
}

// The main function to find two numbers that add up to the target
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    HashTable* table = createHashTable(numsSize * 2); // Larger size to avoid collisions
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int found;
        
        int index = find(table, complement, &found);
        if (found) {
            result[0] = index;
            result[1] = i;
            freeHashTable(table);
            return result;
        }
        
        insert(table, nums[i], i);
    }
    
    freeHashTable(table);
    *returnSize = 0;
    return NULL; // No solution found
}
