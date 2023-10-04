#include "lists.h"


/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If an error occurs - NULL.
 *         Otherwise - a pointer to the inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new_node;

	if (!head)
		return (NULL);

	node = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!node || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node &&
		   node->next &&
		   node->next->n < new_node->n)
		node = node->next;

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
