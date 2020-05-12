import numpy as np
import agents.common_bits as cm


def test_initialize_game_state():

    test_board = cm.initialize_game_state()

    assert isinstance(test_board, np.ndarray)
    assert test_board.dtype == np.int8
    assert test_board.shape == (6, 7)
    assert np.all(test_board == cm.NO_PLAYER)
    return


def test_apply_player_action():

    test_board1_old = cm.initialize_game_state()
    test_board2 = cm.initialize_game_state()

    test_board1_new = cm.apply_player_action(test_board1_old, cm.PlayerAction(3), cm.PLAYER1, True)
    new_row = cm.top_row(test_board1_new, cm.PlayerAction(3))
    old_row = cm.top_row(test_board1_old, cm.PlayerAction(3))
    print('')
    print(cm.pretty_print_board(test_board1_old))
    print('')
    print(cm.pretty_print_board(test_board1_new))
    assert not np.all(test_board1_old == test_board1_new)
    assert new_row != old_row
    test_board1_old = test_board1_new

    test_board1_new = cm.apply_player_action(test_board1_old, cm.PlayerAction(3), cm.PLAYER2, True)
    new_row = cm.top_row(test_board1_new, cm.PlayerAction(3))
    old_row = cm.top_row(test_board1_old, cm.PlayerAction(3))
    assert not np.all(test_board1_old == test_board1_new)
    assert new_row != old_row
    test_board1_old = test_board1_new

    test_board1_new = cm.apply_player_action(test_board1_old, cm.PlayerAction(3), cm.PLAYER1, True)
    new_row = cm.top_row(test_board1_new, cm.PlayerAction(3))
    old_row = cm.top_row(test_board1_old, cm.PlayerAction(3))
    assert not np.all(test_board1_old == test_board1_new)
    assert new_row != old_row
    test_board1_old = test_board1_new

    test_board1_new = cm.apply_player_action(test_board1_old, cm.PlayerAction(3), cm.PLAYER2, True)
    new_row = cm.top_row(test_board1_new, cm.PlayerAction(3))
    old_row = cm.top_row(test_board1_old, cm.PlayerAction(3))
    assert not np.all(test_board1_old == test_board1_new)
    assert new_row != old_row
    test_board1_old = test_board1_new

    test_board1_new = cm.apply_player_action(test_board1_old, cm.PlayerAction(3), cm.PLAYER1, True)
    new_row = cm.top_row(test_board1_new, cm.PlayerAction(3))
    old_row = cm.top_row(test_board1_old, cm.PlayerAction(3))
    assert not np.all(test_board1_old == test_board1_new)
    assert new_row != old_row
    test_board1_old = test_board1_new

    test_board1_new = cm.apply_player_action(test_board1_old, cm.PlayerAction(3), cm.PLAYER2, True)
    try:
        new_row = cm.top_row(test_board1_new, cm.PlayerAction(3))
    except IndexError:
        pass
    old_row = cm.top_row(test_board1_old, cm.PlayerAction(3))
    assert not np.all(test_board1_old == test_board1_new)
    assert new_row == old_row
    test_board1_old = test_board1_new

    try:
        test_board1_new = cm.apply_player_action(test_board1_old, cm.PlayerAction(3), cm.PLAYER1, True)
    except IndexError:
        assert True
    assert np.all(test_board1_old == test_board1_new)
    # test_board1_old = test_board1_new

    test_board2[0, 3] = cm.PLAYER1
    test_board2[1, 3] = cm.PLAYER2
    test_board2[2, 3] = cm.PLAYER1
    test_board2[3, 3] = cm.PLAYER2
    test_board2[4, 3] = cm.PLAYER1
    test_board2[5, 3] = cm.PLAYER2
    assert np.all(test_board1_new == test_board2)


def test_pretty_print_board():

    test_board = cm.initialize_game_state()
    test_board = np.random.randint(0, 3, test_board.shape)
    print('')
    print(test_board)

    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)

    assert isinstance(board_str, str)
    return


def test_string_to_board():

    test_board = cm.initialize_game_state()
    test_board = np.random.randint(0, 3, test_board.shape)
    print('')
    print(test_board)
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    board_arr = cm.string_to_board(board_str)
    print('')
    print(board_arr)

    assert isinstance(test_board, np.ndarray)
    assert board_arr.dtype == np.int8
    assert board_arr.shape == test_board.shape
    return


def test_connect_four_bits():
    # Test a diagonal
    test_board = cm.initialize_game_state()
    test_board[0, 3] = cm.PLAYER1
    test_board[1, 4] = cm.PLAYER1
    test_board[2, 5] = cm.PLAYER1
    test_board[3, 6] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test the same diagonal for the other player
    test_board = cm.initialize_game_state()
    test_board[0, 3] = cm.PLAYER2
    test_board[1, 4] = cm.PLAYER2
    test_board[2, 5] = cm.PLAYER2
    test_board[3, 6] = cm.PLAYER2
    player_map, mask_board = cm.board_to_bitmap(test_board, cm.PLAYER1)
    player_map2 = player_map ^ mask_board
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map2)

    # Rotate the diagonal
    test_board = cm.initialize_game_state()
    test_board[0, 6] = cm.PLAYER1
    test_board[1, 5] = cm.PLAYER1
    test_board[2, 4] = cm.PLAYER1
    test_board[3, 3] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test a row at the top
    test_board = cm.initialize_game_state()
    test_board[5, 3] = cm.PLAYER1
    test_board[5, 4] = cm.PLAYER1
    test_board[5, 5] = cm.PLAYER1
    test_board[5, 6] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test a row at the bottom
    test_board = cm.initialize_game_state()
    test_board[0, 0] = cm.PLAYER1
    test_board[0, 1] = cm.PLAYER1
    test_board[0, 2] = cm.PLAYER1
    test_board[0, 3] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test a column on the left
    test_board = cm.initialize_game_state()
    test_board[2, 0] = cm.PLAYER1
    test_board[3, 0] = cm.PLAYER1
    test_board[4, 0] = cm.PLAYER1
    test_board[5, 0] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test a column on the right
    test_board = cm.initialize_game_state()
    test_board[0, 6] = cm.PLAYER1
    test_board[1, 6] = cm.PLAYER1
    test_board[2, 6] = cm.PLAYER1
    test_board[3, 6] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test some things in the middle
    test_board = cm.initialize_game_state()
    test_board[2, 5] = cm.PLAYER1
    test_board[3, 4] = cm.PLAYER1
    test_board[4, 3] = cm.PLAYER1
    test_board[5, 2] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    test_board = cm.initialize_game_state()
    test_board[0, 2] = cm.PLAYER1
    test_board[1, 3] = cm.PLAYER1
    test_board[2, 4] = cm.PLAYER1
    test_board[3, 5] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test the last_action option for column 6
    test_board = cm.initialize_game_state()
    test_board[0, 3] = cm.PLAYER1
    test_board[1, 4] = cm.PLAYER1
    test_board[2, 5] = cm.PLAYER1
    test_board[3, 6] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test the last_action option for column 5
    test_board = cm.initialize_game_state()
    test_board[0, 2] = cm.PLAYER1
    test_board[1, 3] = cm.PLAYER1
    test_board[2, 4] = cm.PLAYER1
    test_board[3, 5] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test the last_action option for column 1
    test_board = cm.initialize_game_state()
    test_board[0, 1] = cm.PLAYER1
    test_board[1, 1] = cm.PLAYER1
    test_board[2, 1] = cm.PLAYER1
    test_board[3, 1] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test the last_action option for column 2 diagonal pattern
    test_board = cm.initialize_game_state()
    test_board[0, 1] = cm.PLAYER1
    test_board[1, 2] = cm.PLAYER1
    test_board[2, 3] = cm.PLAYER1
    test_board[3, 4] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert cm.connect_four(player_map)

    # Test for overflow issues - horizontal
    test_board = cm.initialize_game_state()
    test_board[0, 4] = cm.PLAYER1
    test_board[0, 5] = cm.PLAYER1
    test_board[0, 6] = cm.PLAYER1
    test_board[1, 0] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert not cm.connect_four(player_map)

    # Test for overflow issues - diagonal
    test_board = cm.initialize_game_state()
    test_board[0, 2] = cm.PLAYER1
    test_board[1, 1] = cm.PLAYER1
    test_board[2, 0] = cm.PLAYER1
    test_board[2, 6] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert not cm.connect_four(player_map)

    # Test for overflow issues - vertical
    test_board = cm.initialize_game_state()
    test_board[3, 1] = cm.PLAYER1
    test_board[3, 2] = cm.PLAYER1
    test_board[3, 3] = cm.PLAYER1
    test_board[4, 0] = cm.PLAYER1
    test_board[2, 0] = cm.PLAYER1
    player_map = cm.board_to_bitmap(test_board, cm.PLAYER1)[0]
    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)
    assert not cm.connect_four(player_map)


def test_board_to_bitmap():

    test_board = cm.initialize_game_state()
    test_board[0, 2] = cm.PLAYER1
    test_board[0, 3] = cm.PLAYER2
    test_board[0, 4] = cm.PLAYER2
    test_board[0, 5] = cm.PLAYER1
    test_board[1, 2] = cm.PLAYER1
    test_board[1, 3] = cm.PLAYER1
    test_board[1, 4] = cm.PLAYER2
    test_board[2, 2] = cm.PLAYER1
    test_board[2, 3] = cm.PLAYER2
    test_board[3, 2] = cm.PLAYER2
    test_board[3, 3] = cm.PLAYER2
    test_board[4, 3] = cm.PLAYER1

    mask_pos = int('000000000000100000001100000011000001110000111100', 2)
    # p1_pos =   int('000000000000100000000000000001000000110000100100', 2)
    p2_pos =   int('000000000000000000001100000010000001000000011000', 2)

    print('')
    print(bin(p2_pos))
    print(bin(cm.board_to_bitmap(test_board, cm.PLAYER2)[0]))
    print(bin(mask_pos))
    print(bin(cm.board_to_bitmap(test_board, cm.PLAYER2)[1]))

    assert cm.board_to_bitmap(test_board, cm.PLAYER2)[0] == p2_pos
    assert cm.board_to_bitmap(test_board, cm.PLAYER2)[1] == mask_pos
    assert cm.board_to_bitmap(test_board, cm.PLAYER1)[0] == \
        (mask_pos ^ p2_pos)


def test_check_end_state():

    test_board = cm.initialize_game_state()
    test_board = np.ones(test_board.shape) * 3
    assert cm.check_end_state(test_board, cm.PLAYER1) == \
        cm.GameState.IS_DRAW

    test_board[0, 1] = cm.PLAYER1
    test_board[1, 2] = cm.PLAYER1
    test_board[2, 3] = cm.PLAYER1
    test_board[3, 4] = cm.PLAYER1
    assert cm.check_end_state(test_board, cm.PLAYER1) == \
        cm.GameState.IS_WIN

    test_board[-1, -1] = cm.NO_PLAYER
    assert cm.check_end_state(test_board, cm.PLAYER1) == \
        cm.GameState.IS_WIN


def test_top_row():

    test_board = cm.initialize_game_state()
    test_board[0, 0] = cm.PLAYER1
    test_board[:6, 1] = cm.PLAYER1
    test_board[:2, 2] = cm.PLAYER1
    test_board[:3, 3] = cm.PLAYER1
    test_board[:4, 4] = cm.PLAYER1

    board_str = cm.pretty_print_board(test_board)
    print('')
    print(board_str)

    assert cm.top_row(test_board, cm.PlayerAction(0)) == 1
    assert cm.top_row(test_board, cm.PlayerAction(2)) == 2
    assert cm.top_row(test_board, cm.PlayerAction(3)) == 3
    assert cm.top_row(test_board, cm.PlayerAction(4)) == 4
    assert cm.top_row(test_board, cm.PlayerAction(5)) == 0
    assert cm.top_row(test_board, cm.PlayerAction(6)) == 0
    try:
        assert not cm.top_row(test_board, cm.PlayerAction(1))
    except IndexError:
        assert True
