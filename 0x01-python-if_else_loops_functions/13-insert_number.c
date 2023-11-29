#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: listint_t double_pointer
 * number: int input
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *temp;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while(current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		temp = current->next;
		current->next = new;
		new->next = temp;
		return (new);
	}
	return (NULL);
}
