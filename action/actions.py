from action.Action import UseAction
from action.action_tag import Tag
from action.wish_twist_generators import generate_n_no_dupes 

def active_gain_gold(value):
    def gain_value(game):
        player = game.active_player()
        player.add_gold_instant(value)

    return gain_value

def active_sub_gold(value):
    def lose_value(game):
        player = game.active_player()
        player.sub_gold_instant(value)
    
    return lose_value

def d12_gold_roll(multiplier):
    def perform_d12_roll(game):
        player = game.active_player()
        roll_result = game.active_player().dice.perform_d12_roll(game)
        player.add_gold_instant(roll_result * multiplier)
    return perform_d12_roll

def gain_gold_for_orange_heads(multiplier):
    def award_for_each_boh(game):
        player = game.active_player()
        orange_head_count = len([p for p in game.victims if p.big_orange_head])
        player.add_gold_instant(orange_head_count * multiplier)
    return award_for_each_boh

def multiply_next_gold_amount(amount, num_uses):
    def apply_modifier(game):
        def multiplier(gold):
            if gold_multiplier_action.num_uses > 0:
                gold_multiplier_action.num_uses -= 1
                return gold * amount 
            return gold

        gold_multiplier_action = UseAction(multiplier, 1, [Tag.INSTANT_GOLD], num_uses)
        for victim in game.victims:
            victim.gold_modifiers.append(gold_multiplier_action)
    return apply_modifier

def big_orange_head_wish():
    def give_head(game): #lol
        player = game.active_player()
        player.big_orange_head = True
    return give_head

def add_wish_option_next(num_additional_options, num_uses):
    def add_wish_option(game):
        def expiring_additional_wish(base, wishes):
            if action.num_uses <= 0:
                print("no more!")
                return []
            action.num_uses -= 1
            print("additional")
            return generate_n_no_dupes(num_additional_options)(base, wishes)
        player = game.active_player()
        action = UseAction(expiring_additional_wish, 2, [Tag.WISH_MODIFIER], num_uses)
        player.wish_generator_action_stack.append(action)
    return add_wish_option
