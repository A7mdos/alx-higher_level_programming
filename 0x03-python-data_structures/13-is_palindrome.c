#include "lists.h"


listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);


/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head,
			  *next,
			  *prev = NULL;

	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}


/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *middle, *reverse;
	size_t i, temp_size = 0;

	if (head == NULL)
		return (1);

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		temp_size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (temp_size / 2) - 1; i++)
		temp = temp->next;

	if ((temp_size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reverse = reverse_listint(&temp);
	middle = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_listint(&middle);

	return (1);
}
