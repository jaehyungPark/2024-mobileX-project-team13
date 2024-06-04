import i18n
import streamlit as st
import os

from utils.init import init_once


if __name__ == '__main__':
    # Init
    init_once()

    # Show title
    st.title(i18n.t('common.title'))

    # Show page description
    st.write(i18n.t('common.description'))

    # Show image if available
    image_path = i18n.t('common.image_url', default=None)
    if image_path:
        image_full_path = os.path.join(os.path.dirname(__file__), image_path)
        st.image(image_full_path)

    # Show github link
    st.write(f'* Github: {i18n.t('common.github')}')
