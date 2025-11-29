---
layout: page
permalink: people.html
style: header
---

<div class="researcher-gallery">
  {% for person in site.data.researchers.staff %}
  <div class="researcher-card" onclick="openModal('{{ person.name | slugify }}')">
    <div class="researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      <div class="hover-overlay">
        More info on {{ person.name }}
      </div>
    </div>
    <div class="researcher-info">
      <h4>{{ person.name }}</h4>
      <p class="title">{{ person.title }}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate" title="ResearchGate">
            <i class="fab fa-researchgate"></i>
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin" title="LinkedIn">
            <i class="fab fa-linkedin-in"></i>
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter" title="Twitter">
            <i class="fab fa-twitter"></i>
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website" title="Website">
            <i class="fas fa-globe"></i>
          </a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<div class="section-title small">
  <h4>Researchers</h4>
</div>

<div class="researcher-gallery">
  {% for person in site.data.researchers.researchers %}
  <div class="researcher-card" onclick="openModal('{{ person.name | slugify }}')">
    <div class="researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      <div class="hover-overlay">
        More info on {{ person.name }}
      </div>
    </div>
    <div class="researcher-info">
      <h4>{{ person.name }}</h4>
      <p class="title">{{ person.title }}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate" title="ResearchGate">
            <i class="fab fa-researchgate"></i>
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin" title="LinkedIn">
            <i class="fab fa-linkedin-in"></i>
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter" title="Twitter">
            <i class="fab fa-twitter"></i>
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website" title="Website">
            <i class="fas fa-globe"></i>
          </a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<div class="section-title">
  <h3>PhD Students</h3>
  <div class="divider"></div>
</div>

<div class="researcher-gallery">
  {% for person in site.data.researchers.phd_students %}
  <div class="researcher-card" onclick="openModal('{{ person.name | slugify }}')">
    <div class="researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      <div class="hover-overlay">
        More info on {{ person.name }}
      </div>
    </div>
    <div class="researcher-info">
      <h4>{{ person.name }}</h4>
      <p class="title">{{ person.title }}{% if person.supervisor %}<br><small>{{ person.supervisor }}</small>{% endif %}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate" title="ResearchGate">
            <i class="fab fa-researchgate"></i>
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin" title="LinkedIn">
            <i class="fab fa-linkedin-in"></i>
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter" title="Twitter">
            <i class="fab fa-twitter"></i>
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website" title="Website">
            <i class="fas fa-globe"></i>
          </a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<!-- Modal for detailed bio -->
{% for person in site.data.researchers.staff %}
<div id="{{ person.name | slugify }}-modal" class="researcher-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div class="modal-researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
    </div>
    <div class="modal-researcher-info">
      <h3>{{ person.name }}</h3>
      <p class="title">{{ person.title }}</p>
      <p class="bio">{{ person.bio }}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate">
            <i class="fab fa-researchgate"></i> ResearchGate
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin">
            <i class="fab fa-linkedin-in"></i> LinkedIn
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter">
            <i class="fab fa-twitter"></i> Twitter
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website">
            <i class="fas fa-globe"></i> Website
          </a>
        {% endif %}
      </div>
    </div>
  </div>
</div>
{% endfor %}

{% for person in site.data.researchers.researchers %}
<div id="{{ person.name | slugify }}-modal" class="researcher-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div class="modal-researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
    </div>
    <div class="modal-researcher-info">
      <h3>{{ person.name }}</h3>
      <p class="title">{{ person.title }}</p>
      <p class="bio">{{ person.bio }}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate">
            <i class="fab fa-researchgate"></i> ResearchGate
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin">
            <i class="fab fa-linkedin-in"></i> LinkedIn
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter">
            <i class="fab fa-twitter"></i> Twitter
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website">
            <i class="fas fa-globe"></i> Website
          </a>
        {% endif %}
      </div>
    </div>
  </div>
</div>
{% endfor %}

{% for person in site.data.researchers.phd_students %}
<div id="{{ person.name | slugify }}-modal" class="researcher-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div class="modal-researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
    </div>
    <div class="modal-researcher-info">
      <h3>{{ person.name }}</h3>
      <p class="title">{{ person.title }}{% if person.supervisor %}<br><small>{{ person.supervisor }}</small>{% endif %}</p>
      <p class="bio">{{ person.bio }}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate">
            <i class="fab fa-researchgate"></i> ResearchGate
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin">
            <i class="fab fa-linkedin-in"></i> LinkedIn
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter">
            <i class="fab fa-twitter"></i> Twitter
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website">
            <i class="fas fa-globe"></i> Website
          </a>
        {% endif %}
      </div>
    </div>
  </div>
</div>
{% endfor %}

### Former PhD students

- Anna Twomlow (2021).
- Charles Zogheib (2021).
- Simon De Stercke (2020).
- Hsi-Kai Chou (2020). Next destination: University of Cardiff.
- Boris Ochoa (2019). Next destionation: ATUK, Ecuador.
- Peter Blair (2018). Now at Thames Water, UK
- Sam Grainger (2018). Now at University of Leeds, UK
- Tilashwork Chanie (2018)
- Xi Liu (2018)
- Jimmy O'Keeffe (2016).
- Bastian Manz (2016). Now at Willis Re, UK
- Simon Moulds (2016). Now at the University of Exeter, UK
- Claudia Vitolo (2015). Now at ECMWF, Reading, UK.
- Gina Tsarouchi (2015). Now at HR Wallingford, UK
- Susana Almeida (2014). Now at University of Bristol, UK
- Zed Zulkafli (2014). Next destination: Universiti Putra Malaysia
- Emma Bergin (2013). Next destination: Flood Re, London, UK

<script>
function openModal(personSlug) {
  const modal = document.getElementById(personSlug + '-modal');
  if (modal) {
    modal.classList.add('active');
  }
}

// Close modal when clicking the X or outside the modal
document.addEventListener('DOMContentLoaded', function() {
  const modals = document.querySelectorAll('.researcher-modal');
  
  modals.forEach(modal => {
    // Close when clicking the X
    const closeBtn = modal.querySelector('.close');
    closeBtn.addEventListener('click', function() {
      modal.classList.remove('active');
    });
    
    // Close when clicking outside the modal content
    modal.addEventListener('click', function(e) {
      if (e.target === modal) {
        modal.classList.remove('active');
      }
    });
  });
  
  // Close with ESC key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      modals.forEach(modal => {
        modal.classList.remove('active');
      });
    }
  });
});
</script>

