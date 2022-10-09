
#include <iostream>
#include "hash_table.h"
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
Based on original work by:
https://gist.github.com/kuriringohankamehameha/fceee2e3c126f37fd254ee0acf2b4633

And his blog:
https://www.digitalocean.com/community/tutorials/hash-table-in-c-plus-plus

And also based on:
https://gist.github.com/oschonrock/d0540347a5a6739a24c4648e724a3e96
*/

namespace hash_table {

// Creates a pointer to a new hash table item
HashTableItem* ht_create_item(ht_key_t key, ht_value_t value) {
  // Needs allocated memory in order to be returned from a function.
  HashTableItem* item = new HashTableItem;
  // -> notation required for pointer to struct (vs struct.attribute)
  item->key           = strdup(key);
  item->value         = value;
  item->next          = nullptr;
  return item;
}

// Creates a new HashTable
HashTable* ht_create(size_t size) {
  HashTable* table = new HashTable;
  table->size      = size;
  table->count     = 0;
  table->items = new HashTableItem*[table->size];
  return table;
}

// Deletes an item
void ht_delete_item(HashTableItem* item) {
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
// and returns nullptr if it doesn't exist.
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

} // End of namespace hash_table
