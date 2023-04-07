#include "hash_tables.h"
#include <stdlib.h>

/**
 * hash_table_create - a function that creates a hash table.
 * @size: is the size of the array
 * Return: a pointer to the newly created hash table
 * If something went wrong, return NULL
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *ht;
	unsigned int i = 0;

	ht = malloc(sizeof(*ht));
	if (ht == NULL)
	{
		return (NULL);
	}
	ht->array = malloc(sizeof(hash_node_t *) * size);
	if (ht->array == NULL)
	{
		free(ht);
		return (NULL);
	}
	ht->size = size;
	while (i < size)
	{
		ht->array[i] = NULL;
		++i;
	}

	return (ht);
}
