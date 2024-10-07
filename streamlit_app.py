import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# ASCII art representation of an octopus
octopus_art = r"""
          _.-=-._     .--.
        .'       '.  |o_o |
       /     .-._  \ |:_/ |
      |    /    \  |    _  |
       \  |      |  |   (_) |
        '._\    /_.'  |     |
           '-..-'     '-----'
"""

# Display the octopus art and emojis
st.markdown("### Here's an octopus for you:")
st.code(octopus_art, language='plaintext')
st.markdown("🐙🐙🐙")  # Display octopus emojis

st.image("image1.png", caption="A beautiful squid/cuttlefish", use_column_width=True)

muhu = r"""🔥☁☀    ☁         🛸☁  ☁
       ☁         🛩                   ✈️
__🏬_🏨__⛩️ 🏫🏢🏪____🏦🏢__🏩___
                 /  |  \.      🤾.   🤸.     🏌️.    
         🌴 /🚔    \ 🌴👫🏻 🏃      🤼.   
             /      |      \.           ⛹️
     🌴 /🚔      🚔 \ 🌴
         / 🚖    |    🚘 \          🚶‍♂️🚶‍♀️    🏃‍♂️
⛽  /  🚔      🚘       \
🌴/            🚔            \ 🚦    
__/                                \___________                                                                                                        __      ️   __  🚗 __  🚕   __ 🚓 __ 🚑 _ 🚒  _
__ __ 🚙💨💨💨🚓____ 🚓 ___🚐__🚓_________🚚____🚛   __   🚓 __  🚴‍♂️"""

st.markdown("### Here's a cuckoo bird made with octopus emojis:")
st.code(muhu, language='plaintext')

cuckoo_art = r"""
          🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙
        🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙
      🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙
        🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙
          🐙🐙🐙🐙🐙🐙🐙
            🐙🐙🐙🐙
           🐙🐙🐙🐙🐙
          🐙🐙🐙🐙🐙🐙🐙
         🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙
        🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙
             🐙🐙🐙🐙🐙
             🐙🐙🐙🐙🐙
           🐙🐙🐙🐙🐙🐙🐙
         🐙🐙🐙🐙🐙🐙🐙🐙🐙🐙
"""

# Display the cuckoo art
st.markdown("### Here's a cuckoo bird made with octopus emojis:")
st.code(cuckoo_art, language='plaintext')

st.image("image.png", caption="A beautiful squid/cuttlefish", use_column_width=True)