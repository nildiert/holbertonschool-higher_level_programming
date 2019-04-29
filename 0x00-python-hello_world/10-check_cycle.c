#include "lists.h"

/**
 * check_cycle - Entry point
 *
 * @list: List that receives
 * Return: Always 0 (Success)
 */

int check_cycle(listint_t *list)
{
	listint_t *same_1 = list;
	listint_t *same_2 = list;

	if (list != NULL)
	{
		same_2 = same_2->next;
		while ((same_1 != NULL && same_2 != NULL) || same_2->next != NULL)
		{
			if (same_2 == same_1)
				return (1);
			if (same_2->next != NULL && same_1->next != NULL)
			{
				same_2 = same_2->next->next;
				same_1 = same_1->next;
			}
			else
				return (0);
		}
	}
	return (0);
}
