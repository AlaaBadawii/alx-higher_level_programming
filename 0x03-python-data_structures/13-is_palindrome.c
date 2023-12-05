#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: listint_t double_pinter
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *original_head = *head;
	listint_t *runner = *head;
	int len, i;
	int *str;

	if (original_head == NULL)
		return (1);

	len = 0;
	while (runner != NULL)
	{
		runner = runner->next;
		len++;
	}
	str = malloc(sizeof(int) * len / 2);
	for (i = 0; i < len / 2; i++)
	{
		str[i] = original_head->n;
		original_head = original_head->next;
	}
	if (len % 2 != 0)
	{
		original_head = original_head->next;
		len--;
	}
	for (i = len / 2 - 1; i >= 0; i--)
	{
		if (original_head->n != str[i])
		{
			free(str);
			return (0);
		}
		original_head = original_head->next;
	}
	free(str);

	return (1);
}
