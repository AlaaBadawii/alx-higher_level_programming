#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: listint_t pointer
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tortise, *hare;

	hare = list;
	tortise = list;

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tortise = tortise->next;

		if (hare == tortise)
			return (1);
	}

	return (0);
}

