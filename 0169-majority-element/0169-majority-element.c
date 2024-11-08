
typedef struct {
    int key;   // The number
    int count; // Frequency of the number
} KeyValuePair;

typedef struct {
    KeyValuePair* data;
    int capacity;
    int size;
} Bucket;

typedef struct {
    Bucket* buckets;
    int bucketCount;
} HashTable;

#define INITIAL_CAPACITY 4

// Hash function to get index for a given key
int hashFunction(int key, int bucketCount) {
    return abs(key) % bucketCount;
}

// Initialize a bucket
void initBucket(Bucket* bucket) {
    bucket->data = (KeyValuePair*)malloc(INITIAL_CAPACITY * sizeof(KeyValuePair));
    bucket->capacity = INITIAL_CAPACITY;
    bucket->size = 0;
}

// Resize a bucket if it's full
void resizeBucket(Bucket* bucket) {
    bucket->capacity *= 2;
    bucket->data = (KeyValuePair*)realloc(bucket->data, bucket->capacity * sizeof(KeyValuePair));
}

// Insert a key into the hash table
void insert(HashTable* table, int key) {
    int index = hashFunction(key, table->bucketCount);
    Bucket* bucket = &table->buckets[index];

    for (int i = 0; i < bucket->size; ++i) {
        if (bucket->data[i].key == key) {
            bucket->data[i].count++;
            return;
        }
    }

    // If the key is not found, add a new key-value pair
    if (bucket->size == bucket->capacity) {
        resizeBucket(bucket);
    }

    bucket->data[bucket->size].key = key;
    bucket->data[bucket->size].count = 1;
    bucket->size++;
}

// Initialize the hash table
HashTable* createHashTable(int bucketCount) {
    HashTable* table = (HashTable*)malloc(sizeof(HashTable));
    table->bucketCount = bucketCount;
    table->buckets = (Bucket*)malloc(bucketCount * sizeof(Bucket));

    for (int i = 0; i < bucketCount; ++i) {
        initBucket(&table->buckets[i]);
    }

    return table;
}

// Free memory allocated for the hash table
void freeHashTable(HashTable* table) {
    for (int i = 0; i < table->bucketCount; ++i) {
        free(table->buckets[i].data);
    }
    free(table->buckets);
    free(table);
}

// Find the majority element in the array
int majorityElement(int* nums, int numsSize) {
    HashTable* table = createHashTable(numsSize);

    // Insert elements into the hash table and count frequencies
    for (int i = 0; i < numsSize; ++i) {
        insert(table, nums[i]);
    }

    int majority = -1;
    for (int i = 0; i < table->bucketCount; ++i) {
        Bucket* bucket = &table->buckets[i];
        for (int j = 0; j < bucket->size; ++j) {
            if (bucket->data[j].count > numsSize / 2) {
                majority = bucket->data[j].key;
                break;
            }
        }
        if (majority != -1) break;
    }

    // Free allocated memory
    freeHashTable(table);
    return majority;
}
