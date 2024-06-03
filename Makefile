NAME_GAME_OF_LIFE = game_of_life
NAME_LENIA = lenia

all: game_of_life lenia

game_of_life:
	cp game_of_life.py $(NAME_GAME_OF_LIFE)
	chmod +x $(NAME_GAME_OF_LIFE)

lenia:
	cp lenia.py $(NAME_LENIA)
	chmod +x $(NAME_LENIA)

clean:
	rm -rf $(NAME_GAME_OF_LIFE)
	rm -rf $(NAME_LENIA)

re: clean all

.PHONY: all game_of_life lenia clean re