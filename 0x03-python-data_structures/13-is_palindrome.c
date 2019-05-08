#include "lists.h"
/**
 * listint_len - Print the list of a single list
 * @h: The pointer of the list
 *
 * Return: The number of elements in the list
 */


size_t listint_len(const listint_t *h)
{
	int i = 0;

	while (h)
	{
		h = h->next;
		i++;
	}
	return (i);
}

/**
 * is_palindrome - check the code for Holberton School students.
 *
 * @head: list
 * Return: Always 0.
 */

int is_palindrome(listint_t **head)
{
	int len, array[1000000], i, j;

	(void)head;
	len = listint_len(*head);
	for (i = 0; i <= len - 1; i++)
	{
		array[i] = (*head)->n;
		(*head) = (*head)->next;
	}
	i--;
	for (j = 0, i; j < len; j++, i--)
	{
		if (array[j] != array[i])
		{
			return (0);
		}
	}
	return (1);
}
