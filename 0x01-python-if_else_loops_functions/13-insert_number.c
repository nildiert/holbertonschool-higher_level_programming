#include "lists.h"

/**
 * *insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copy;
	listint_t *new = malloc(sizeof(*head));
	listint_t *aux;

	if (!head)
		return (0);
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	copy = *head;
	if (number <= 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (copy->n < (number))
	{
		aux = copy;
		if (copy->n < number && copy->next == NULL)
			break;
		copy = copy->next;
	}
	new->next = aux->next;
	aux->next = new;
	return (new);
}