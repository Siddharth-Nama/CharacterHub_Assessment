<template>
  <div class="container" @mousemove="updateCursor">
    <!-- Cinematic Background -->
    <div
      class="background"
      :style="{ backgroundImage: `url(${movie.Poster})`, transform: `scale(${scale})` }"
    ></div>

    <!-- Glass Poster -->
    <div class="poster glass" ref="poster">
      <img :src="movie.Poster" alt="poster" />
    </div>

    <!-- Info Block -->
    <div class="info glass" ref="info">
      <h1 class="movie-title">{{ movie.Title }} <span>({{ movie.Year }})</span></h1>

      <p><strong>Genre:</strong> {{ movie.Genre }}</p>
      <p><strong>Runtime:</strong> {{ movie.Runtime }}</p>

      <div class="trailer-container" @mouseenter="playTrailer" @mouseleave="pauseTrailer">
        <button class="neon-button">▶ Play Trailer</button>
        <video
          v-if="trailerPlaying"
          class="trailer-preview"
          autoplay
          muted
          loop
          playsinline
          :src="trailerUrl"
        ></video>
      </div>

      <h3>Overview</h3>
      <p>{{ movie.Plot }}</p>

      <h4>Director</h4>
      <p>{{ movie.Director }}</p>

      <h4>Writers</h4>
      <p>{{ movie.Writer }}</p>

      <h4>Cast</h4>
      <p>{{ movie.Actors }}</p>
    </div>

    <!-- Floating HUD Ribbon -->
    <div class="film-stats">
      🎬 IMDb: 7.8 | 🍅 Rotten: 85% | 🔥 Popularity: High
    </div>

    <!-- Custom Cursor -->
    <div class="custom-cursor" :style="{ left: cursorX + 'px', top: cursorY + 'px' }"></div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import { gsap } from "gsap";

export default {
  data() {
    return {
      movie: {},
      scale: 1,
      trailerPlaying: false,
      trailerUrl: "https://www.w3schools.com/html/mov_bbb.mp4", 
      cursorX: 0,
      cursorY: 0,
    };
  },
  mounted() {
    fetch("http://www.omdbapi.com/?i=tt3896198&apikey=d2132124")
      .then((res) => res.json())
      .then((data) => {
        this.movie = data;
      });

    // GSAP animation for cinematic feel
    gsap.from(this.$refs.poster, {
      y: 100,
      opacity: 0,
      duration: 1,
      delay: 0.3,
      ease: "power3.out",
    });

    gsap.from(this.$refs.info, {
      y: 200,
      opacity: 0,
      duration: 1.2,
      delay: 0.6,
      ease: "power4.out",
    });

    window.addEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const scrollY = window.scrollY;
      this.scale = 1 + scrollY * 0.0005;
    },
    playTrailer() {
      this.trailerPlaying = true;
    },
    pauseTrailer() {
      this.trailerPlaying = false;
    },
    updateCursor(e) {
      this.cursorX = e.clientX;
      this.cursorY = e.clientY;
    },
  },
};
</script>

<style scoped>
.container {
  position: relative;
  overflow-x: hidden;
  min-height: 100vh;
  padding: 40px;
  color: white;
}

/* Background Parallax */
.background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  filter: blur(15px) brightness(0.5);
  z-index: -1;
  transition: transform 0.3s ease;
}

/* Glass Effect */
.glass {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  padding: 20px;
  margin: 20px;
  transition: transform 0.4s ease;
}

.poster img {
  border-radius: 15px;
  max-width: 100%;
}

.movie-title {
  font-size: 2rem;
  animation: fadeIn 1s ease-in-out forwards;
}

/* Neon Button with Video Preview */
.trailer-container {
  position: relative;
}
.neon-button {
  background: #00e0ff;
  color: black;
  font-weight: bold;
  padding: 12px 24px;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  box-shadow: 0 0 10px #00e0ff, 0 0 20px #00e0ff;
}
.trailer-preview {
  position: absolute;
  top: 110%;
  left: 0;
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 15px;
  z-index: 3;
}

/* Floating HUD */
.film-stats {
  position: fixed;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(10, 10, 10, 0.75);
  padding: 8px 16px;
  border-radius: 30px;
  font-size: 14px;
  color: #00e0ff;
  font-family: 'Courier New', monospace;
  box-shadow: 0 0 10px #00e0ff;
  z-index: 1000;
}

/* Custom Cursor */
.custom-cursor {
  width: 15px;
  height: 15px;
  background-color: #00e0ff;
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  box-shadow: 0 0 10px #00e0ff, 0 0 20px #00e0ff;
  transform: translate(-50%, -50%);
  transition: transform 0.1s ease;
}

/* Responsive */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
</style>
