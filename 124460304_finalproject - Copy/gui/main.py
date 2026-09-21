import pygame
from shooter import Shooter
from centipede import Centipede
from dart import Dart
from eventlist import EventList

pygame.init()

right_was_held = False
left_was_held = False

DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 850
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
display = pygame.display.set_mode(DISPLAY_SIZE)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

shooter = Shooter(180, 800, 40, 7, white)
centipede = Centipede(0, 50, 40, 3, red)
dart = Dart(10, 10, white)

event_list = EventList(max_events=8)

run_game = True
while run_game:
    display.fill(black)

    shooter.draw(display)
    centipede.draw(display)
    dart.draw(display)

    centipede.move()
    centipede.collide(DISPLAY_SIZE)
    centipede.collide_with_dart(DISPLAY_SIZE, dart, event_list)

    if centipede.get_y() > DISPLAY_HEIGHT // 2:
        centipede.relocate(DISPLAY_SIZE)
        event_list.add_event("Centipede reached halfway")

    if dart.is_active():
        dart.fire(DISPLAY_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                event_list.print_events()

        if event.type == pygame.QUIT:
            run_game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dart.set_position([shooter.get_x(), shooter.get_y()])
                dart.activate()
                event_list.add_event("Dart fired")

            if event.key == pygame.K_e:
                event_list.print_events()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        shooter.move_right(DISPLAY_SIZE)
        if not right_was_held:
            event_list.add_event("RIGHT held")
            right_was_held = True
    else:
        right_was_held = False

    if keys[pygame.K_LEFT]:
        shooter.move_left()
        if not left_was_held:
            event_list.add_event("LEFT held")
            left_was_held = True
    else:
        left_was_held = False

    pygame.display.update()
    clock.tick(40)

pygame.quit()
quit()
