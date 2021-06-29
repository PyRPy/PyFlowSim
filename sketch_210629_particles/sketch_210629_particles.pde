// simple particle system
// https://processing.org/examples/simpleparticlesystem.html

ParticleSystem ps;

void setup() {
  size(640, 360);
  ps = new ParticleSystem(new PVector(width/2, 50));
}

void draw() {
  background(0);
  ps.addParticle();
  ps.run();
}

// class of group of particles
class ParticleSystem {
  ArrayList<Particle> particles;
  PVector origin;
  
  ParticleSystem(PVector position) {
    origin = position.copy();
    particles = new ArrayList<Particle>();
  }
  
  void addParticle() {
    particles.add(new Particle(origin));
  }
  
  void run() {
    for (int i = particles.size() - 1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.run();
      if (p.isDead()) {
        particles.remove(i);
      }
    }
  }
}


// a simple particle class
class Particle {
  PVector position;
  PVector velocity;
  PVector acceleration;
  float lifespan;
  
  Particle(PVector l) {
    acceleration = new PVector(0, 0.05);
    velocity = new PVector(random(-1, 1), random(-2, 0));
    position = l.copy();
    lifespan = 255.0;
  }
  
  
  void run() {
    update();
    display();
  }
  
  // update position
  void update() {
    velocity.add(acceleration);
    position.add(velocity);
    lifespan -= 1.0;
  }
  
  // method to display
  void display() {
    stroke(255, lifespan);
    fill(255, lifespan);
    ellipse(position.x, position.y, 8, 8);
  }
  
  // is particle still alive
  boolean isDead() {
    if (lifespan < 0.0) {
      return true;
    } else {
      return false;
    }
  }
}
