#include <stdio.h>
#include <stdlib.h>

double execute_op(double* stack, int stack_idx, char op){
	switch(op){
		case '+':
			return stack[stack_idx - 1] + stack[stack_idx];
		case '-':
			return stack[stack_idx - 1] - stack[stack_idx];
		case '*':
			return stack[stack_idx - 1] * stack[stack_idx];
		case '/':
			if(stack[stack_idx] != 0){
				return stack[stack_idx - 1] / stack[stack_idx];
			}
			else{
				return 0;
			}
	}
	//To make the compiler happy, shouldn't ever hit it though.
	return -1;
}

int main(int argc, char** argv){
	int stack_sz = 0;
	int max_stack_sz = 16;
	double* stack = malloc(sizeof(double) * max_stack_sz);
	double num = 0;

	char add_num = 0;
	char c;
	while((c = getc(stdin)) != '\n' && c != EOF){
		//Continue parsing number
		if(c >= '0' && c <= '9'){
			num *= 10;
			num += c - 48;
			add_num = 1;
		}
		//Add the number to the stack
		else if(c == ' '){
			if(add_num){
				//Readjust the stack size if it isn't large enough
				if(stack_sz == max_stack_sz){
					max_stack_sz *= 2;
					stack = realloc(stack, sizeof(double) * max_stack_sz);
				}
				stack[stack_sz++] = num;
				num = 0;
			}
			add_num = 0;
		}
		//Operators
		else if(c == '+' || c == '-' || c == '*' || c == '/'){
			if(stack_sz <= 1){
				printf("Invalid Input\n");
				return -1;
			}
			stack_sz--;
			stack[stack_sz - 1] = execute_op(stack, stack_sz, c);
			if(c == '/' && stack[stack_sz - 1] == 0){
				printf("Invalid Input\n");
				return -1;
			}
		}
		else{
			printf("Invalid Input\n");
			return -1;
		}
	}
	if(stack_sz == 1 && add_num == 0){
		printf("%.4lf\n", stack[0]);
		return 0;
	}
	else if(stack_sz > 1 || (stack_sz == 1 && add_num == 1)){
		printf("Invalid Input\n");
		return -1;
	}
	else if(stack_sz == 0 && add_num == 1){
		printf("%.4lf\n", num);
		return 0;
	}
	printf("Invalid Input\n");
	return -1;
}
