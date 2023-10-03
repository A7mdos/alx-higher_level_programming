#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle (loop) in it.
 *
 * @list: A pointer to the head of the linked list.
 *
 * Return: If there is no cycle - 0.
 *		   Otherwise - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle,
			  *rabbit;

	turtle = list;
	rabbit = list;

	while (turtle && rabbit && rabbit->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;

		if (turtle == rabbit)
			return (1);
	}

	return (0);
}
