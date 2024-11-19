/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './main/templates/Main/**/*.html',
    './main/templates/**/*.html',  // Make sure to add the paths to your templates here
    './main/static/js/**/*.js',
    './Zapcommerce/**/*.py',
  ],
  theme: {
    extend: {
      //Height

      minHeight : {
        '50vh' : '50vh'
      },

      //Color
      colors : {
        'primary' : '#2C3E50',
        'secondary' : '#E74C3C',
        'accent' : '#F1C40F',
        'background' : '#F8F9FA',
        'text-color' : '#333333',
        'border' : '#BDC3C7',
        'light-silver' : '#ECF0F1'
      },

      //fonts
      fontFamily : {
        'play-fair' : ['Playfair Display', 'serif'],
        'lato' : ['Lato', 'sans-serif']
      },
      fontWeight: {
        '400': '400',
        '500': '500',
        '600': '600',
        '700': '700',
        '800': '800',
        '900': '900',
      }
    },
  },
  plugins: [
    require('@tailwindcss/line-clamp')
  ],
}

