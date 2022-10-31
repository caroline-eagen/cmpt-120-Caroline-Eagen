import pygame



WIDTH = 550
background_color = (251, 247, 245)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    
    for i in range(0, 10):
        pygame.draw.line(win, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
        pygame.draw.line(win, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)
        
        
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
main()