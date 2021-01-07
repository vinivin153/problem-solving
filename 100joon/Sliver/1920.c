#include <stdio.h>
#include<stdlib.h>

typedef struct BST
{
    int x;
    struct BST *left;
    struct BST *right;
} BST;

BST *insert_new(int data);
BST *insert_data(BST *root, int data);
int find_data(BST *root, int find);

int main()
{
    BST *root = NULL;
    int n, m, data;

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d",&data);
        root = insert_data(root, data);
    }

    scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        scanf("%d",&data);
        printf("%d\n", find_data(root, data));
    }
}

BST *insert_new(int data)
{
    BST *newnode = malloc(sizeof(BST));
    newnode->x = data;
    newnode->left = NULL;
    newnode->right = NULL;

    return newnode;
}

BST *insert_data(BST *root, int data)
{
    if (root == NULL)
        root = insert_new(data);
    else
    {
        if (root->x > data)
        {
            if (root->left == NULL)
                root->left = insert_new(data);
            else
                insert_data(root->left, data);
        }
        else
        {
            if (root->right == NULL)
                root->right = insert_new(data);
            else
                insert_data(root->right, data);
        }
    }
    return root;
}

int find_data(BST *root, int find)
{
    if (root == NULL)
        return 0;
    else
    {
        if (root->x == find)
            return 1;
        else if (root->x > find)
            find_data(root->left, find);
        else
            find_data(root->right, find);
    }
}