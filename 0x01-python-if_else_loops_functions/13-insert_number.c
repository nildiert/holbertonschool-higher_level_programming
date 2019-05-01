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
	listint_t *new;
	listint_t *aux;

	if (!head)
		return (0);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);
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
	while (copy)
	{
		if (copy->n < number)
		{
			aux = copy;
			copy = copy->next;
		}
		else
			break;
	}
	new->next = aux->next;
	aux->next = new;
	return (new);
}
