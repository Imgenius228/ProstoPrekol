import play

# спрайт (по умолчанию улыбается)
player = play.new_image(image='4.png', x=0, y=0, size = 100)
speech = play.new_text(words="Привет", x = 0, y = -play.screen.height/2 + 20) # Наш текст для гравця. Який ми потім змінюємо


@play.when_program_starts
def start(): 
    tutorial = play.new_text(words = "п-рассказать шутку, ц-поесть, н-погладить, у-играть в компуктер, к-пойти в магаз, е-сфоткатся, я-закончить игру ", x = 0, y = 250, font_size = 20)
    # Тут ми робимо стартові дії. Наприклад напис з управлінням:

    #tutorial = play.new_text(



@play.repeat_forever 
async def do ():
    # Тут цикл в якому перевіряємо нажаті клавіші
    if play.key_is_pressed('п') or play.key_is_pressed('П') or play.key_is_pressed('w') or play.key_is_pressed('W'): # Дві умови бо може бути ввімкнен капс лок(Також можно додати ямову для анг. мови)
        player.image = '4.png'
        speech.words = 'Ану давай рассказывай'
        player.size = 120
        await play.timer(seconds = 2.0)
        player.image = '5.png'
        speech.words = 'АХХАХАХА очень смешно'

    if play.key_is_pressed('Ц') or play.key_is_pressed('ц'):
        player.image = '6.png'
        player.size = 30
        speech.words = '"Звуки чавкания"' 
        await play.timer(seconds = 2.0)
        player.size = 100  
        player.image = '3.png'
        speech.words = 'Спасибо, очень вкусно, я наелся'
        
    if play.key_is_pressed('у') or play.key_is_pressed('У'):
        player.size = 130
        player.image = '8.png'
        speech.words = ''
        await play.timer(seconds = 2.0)  
        player.image = '9.png'
        speech.words = 'Есс, минус три йохуу'
        
    if play.key_is_pressed('К') or play.key_is_pressed('к'):
        player.size = 120
        player.image = '7.png'
        speech.words = 'Иду в магазин за чипсеками'
        await play.timer(seconds = 2.0)  
        player.image = '12.png'
        speech.words = 'Увидел что магаз закрытый'  
        await play.timer(seconds = 2.0)
        player.image = '13.png'
        speech.words = '"Хнык хнык"'
        
        
    if play.key_is_pressed('Е') or play.key_is_pressed('е'):
        player.size = 120
        player.image = '11.png'
        speech.words = '"Щелк"'
        
        
    if play.key_is_pressed('Н') or play.key_is_pressed('н'):
        player.size = 120
        player.image = '2.png'
        speech.words = 'Спасибо'
    # І так далі

    # Завершення гри
    if play.key_is_pressed('я'):
        player.image = '1.png'
        speech.words = 'НЕЕЕЕЕЕЕТ не уходи!'
        await play.timer(seconds = 2.0)
        exit() # Для завершення програми

play.start_program()
