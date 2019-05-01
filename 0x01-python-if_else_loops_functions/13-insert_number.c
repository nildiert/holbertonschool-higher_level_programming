#include "lists.h"

/**
 * *add_nodeint - Print the list of a single list
 * @n: The variable of int type that receives
 * @head: The pointer of the list
 *
 * Return: The number of elements in the list
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new = malloc(sizeof(head));
	listint_t *copy = *head;

	if (!new)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (*head);
	}
	else
	{
		new->next = copy;
		*head = new;
	}
	return (*head);
}

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
		return (add_nodeint(head, number));
	while (copy->n < (number))
	{
		aux = copy;

		if (copy->n < number && copy->next == NULL)
			return (add_nodeint_end(&copy, number));
		copy = copy->next;
	}
	new->next = aux->next;
	new->n = number;
	aux->next = new;
	return (new);


}
