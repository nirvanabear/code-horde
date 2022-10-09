
#include <iostream>
// If any C++ libraries are included, even an unnecessary one, code
// compiles ok.

// #include <cstdlib>
// #include <cstring>
// #include <cstdio>
// These libraries should be required, but can be skipped if any C++
// library is included. Using just these, however, causes nullptr
// to malfunction. In all cases, __cplusplus == 199711

using namespace std;

/*
Source:
https://gist.github.com/oschonrock/d0540347a5a6739a24c4648e724a3e96

// #include <stdbool.h>
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// Library set from original code

Which is based on original work by:
https://gist.github.com/kuriringohankamehameha/fceee2e3c126f37fd254ee0acf2b4633

And his blog:
https://www.digitalocean.com/community/tutorials/hash-table-in-c-plus-plus

*/

typedef const char* ht_key_t;
typedef int ht_value_t;

// key => value plus pointer to next item for hash collisions
typedef struct HashTableItem HashTableItem;
struct HashTableItem {
  ht_key_t       key;
  ht_value_t     value;
  HashTableItem* next;
};

// Contains an array of pointers to HashTableItems
typedef struct HashTable {
  HashTableItem** items;
  size_t          size;
  size_t          count; // could be used for rehashing in future
} HashTable; // Alternate way of using typedef

// Creates a pointer to a new hash table item
HashTableItem* ht_create_item(ht_key_t key, ht_value_t value) {
  // Needs allocated memory in order to be returned from a function.
  HashTableItem* item = new HashTableItem;
  // HashTableItem* item = (HashTableItem*) malloc(sizeof *item);
  // -> notation required for pointer to struct (vs struct.attribute)
  item->key           = strdup(key);
  item->value         = value;
  item->next          = nullptr;
  return item;
}

// Creates a new HashTable
HashTable* ht_create(size_t size) {
  HashTable* table = new HashTable;
  // HashTable* table = (HashTable*) malloc(sizeof *table);
  table->size      = size;
  table->count     = 0;
  table->items = new HashTableItem*[table->size];
  // table->items = (HashTableItem**) calloc(table->size, sizeof *table->items); // NOLINT sizeof ptr
  return table;
}

// Deletes an item
void ht_delete_item(HashTableItem* item) {
  // free(item->key); // Not needed after char* changed to const char*
  // free(item);
  delete item;
  item = nullptr;
}

// Frees the whole hashtable
void ht_free(HashTable* table) {
  // Frees the table
  for (size_t i = 0; i < table->size; i++) {
    HashTableItem* item = table->items[i];
    while (item) {
      HashTableItem* next = item->next;
      ht_delete_item(item);
      item = next;
    }
  }
  delete table->items;
  table->items = nullptr;
  delete table;
  table = nullptr;

  // free(table->items);
  // free(table);
}

size_t hash_function(HashTable* table, const char* str) {
  size_t sum = 0;
  for (size_t j = 0; str[j]; ++j) sum += str[j];
  return sum % table->size;
}

// Inserts (or updates if exists) an item
void ht_insert(HashTable* table, ht_key_t key, ht_value_t value) {
  // Creates a pointer to a pointer.
  HashTableItem** slot = &table->items[hash_function(table, key)];
  HashTableItem*  item = *slot;
  if (!item) table->count++;  // HashTable accounting (while will not run)
  while (item) {
    if (strcmp(item->key, key) == 0) {
      item->value = value; // exists, update value
      return;
    }
    slot = &item->next;
    item = *slot;
  }
  *slot = ht_create_item(key, value);
}

// Deletes an item from the table
void ht_delete(HashTable* table, ht_key_t key) {
  HashTableItem** slot = &table->items[hash_function(table, key)];
  HashTableItem*  item = *slot;
  bool is_direct_slot = true;
  while (item) {
    if (strcmp(item->key, key) == 0) {
      *slot = item->next; // remove item from linked list
      ht_delete_item(item);
      if (is_direct_slot) --table->count; // HashTable accounting
      return;
    }
    slot = &item->next;
    item = *slot;
    is_direct_slot = false;
  }
}

// Searches the key in the hashtable
// and returns nullptr if it doesn't exist
HashTableItem* ht_search(HashTable* table, ht_key_t key) {
  HashTableItem* item = table->items[hash_function(table, key)];

  while (item) {
    if (strcmp(item->key, key) == 0) return item;
    item = item->next;
  }
  return nullptr;
}

void ht_print(HashTable* table) {
  printf("\n---- Hash Table ---\n");
  for (size_t i = 0; i < table->size; i++) {
    printf("@%zu: ", i);
    HashTableItem* item = table->items[i];
    while (item) {
      printf("%s => %d | ", item->key, item->value);
      item = item->next;
    }
    printf("\n");
  }
  printf("-------------------\n");
}

void ht_print_search(HashTable* table, ht_key_t key) {
  HashTableItem* val;
  if ((val = ht_search(table, key)) == nullptr) {
    printf("Key:%s does not exist\n", key);
    return;
  }
  printf("Key:%s => %d\n", key, val->value);
}

int main() {
  HashTable* ht = ht_create(3);
  ht_insert(ht, "1", 10);
  ht_insert(ht, "2", 20);
  ht_insert(ht, "Hel3", 30);
  ht_insert(ht, "Cau4", 40);
  ht_insert(ht, "Cau6", 60);

  ht_print_search(ht, "1");
  ht_print_search(ht, "2");
  ht_print_search(ht, "3");
  ht_print_search(ht, "Hel3");
  ht_print_search(ht, "Cau4");
  ht_insert(ht, "Cau4", 61); // update
  ht_print_search(ht, "Cau4");

  ht_print(ht);
  ht_delete(ht, "Hel3");
  ht_delete(ht, "Cau6");
  ht_delete(ht, "1");
  ht_print(ht);

  ht_free(ht);

  printf("C++ version: %ld\n", __cplusplus);

  return 0;
}