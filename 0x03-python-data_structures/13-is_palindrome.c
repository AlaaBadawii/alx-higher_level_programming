#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: listint_t double_pinter
 * Return: Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *temp;
	int len, i, *str;

	current = *head;
	temp = *head;

	if (head == NULL *head == NULL)
		return (1);
	while (temp != NULL)
	{
		temp = temp->next;
		len++;
	}
	str = malloc(sizeof(int) * len / 2);
	for (i = 0; i < len / 2; i++)
	{
		str[i] = current->n;
		current = current->next;
	}
	if (len % 2 != 0)
	{
		current = current->next;
		len--;
	}
	for (i = len / 2 - 1; i >= 0; i--)
	{
		if (current->n != str[i])
		{
			free(str);
			return (0);
		}
		current  = current->next;
	}
	free(str);

	return (1);
}
