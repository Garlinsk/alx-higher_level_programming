#include "lists.h"

size_t list_len(listint_t *head);

listint_t *add_node(listint_t **head, int num);

/**
 * is_palindrome - Checks if a singly linked list is a palidrome
 * @head: The start of the list
 *
 * Return: 1 if is or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *tmp_head = NULL;
	listint_t *tmp_current = NULL;
	size_t i = 0, len = list_len(*head);

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (i < (len / 2))
	{
		add_node(&tmp_head, current->n);
		current = current->next;
		i++;
	}
	if ((len % 2) != 0)
	{
		current = current->next;
		i++;
	}
	tmp_current = tmp_head;
	while (i < len)
	{
		if (tmp_current->n == current->n)
		{
			current = current->next;
			tmp_current = tmp_current->next;
		}
		else
		{
			free_listint(tmp_head);
			return (0);
		}
		i++;
	}
	free_listint(tmp_head);
	return (1);
}

/**
 * list_len - Goes through a listint_t list
 * @head: The first node of the list
 *
 * Return: Always an unsigned int, the total number of nodes
 */
size_t list_len(listint_t *head)
{
	unsigned int total = 0;
	listint_t *current = head;

	if (head == NULL)
		return (0);

	while (current)
	{
		total++;
		current = current->next;
	}

	return (total);
}

/**
 * add_node - Adds a new node at the beginning of a list
 * @head: The first node of a list
 * @num: The integer for the new node
 *
 * Return: The address of the new node or NULL
 */
listint_t *add_node(listint_t **head, int num)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = num;
	new->next = *head;
	*head = new;

	return (*head);
}
