---
layout: page
permalink: people.html
style: header
---

<div class="researcher-gallery">
  {% for person in site.data.researchers.staff %}
  <div class="researcher-card staff-card" onclick="openModal('{{ person.name | slugify }}')">
    <div class="researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      <div class="hover-overlay">
        More info<br>{{ person.name }}
      </div>
    </div>
    <div class="researcher-info">
      <h4>{{ person.name }}</h4>
      <p class="title">{{ person.title }}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate" title="ResearchGate" onclick="event.stopPropagation()">
            <i class="fab fa-researchgate"></i>
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin" title="LinkedIn" onclick="event.stopPropagation()">
            <i class="fab fa-linkedin-in"></i>
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter" title="Twitter" onclick="event.stopPropagation()">
            <i class="fab fa-twitter"></i>
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website" title="Website" onclick="event.stopPropagation()">
            <i class="fas fa-globe"></i>
          </a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>

<div class="section-title">
  <h3>Researchers</h3>
  <div class="divider"></div>
</div>

<div class="researcher-gallery">
  {% for person in site.data.researchers.researchers %}
  <div class="researcher-card" onclick="openModal('{{ person.name | slugify }}')">
    <div class="researcher-image">
      <img src="{{ '/assets/img/' | append: person.image | relative_url }}" alt="{{ person.name }}">
      <div class="hover-overlay">
        More info<br>{{ person.name }}
      </div>
    </div>
    <div class="researcher-info">
      <h4>{{ person.name }}</h4>
      <p class="title">{{ person.title }}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate" title="ResearchGate" onclick="event.stopPropagation()">
            <i class="fab fa-researchgate"></i>
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin" title="LinkedIn" onclick="event.stopPropagation()">
            <i class="fab fa-linkedin-in"></i>
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter" title="Twitter" onclick="event.stopPropagation()">
            <i class="fab fa-twitter"></i>
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website" title="Website" onclick="event.stopPropagation()">
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
        More info<br>{{ person.name }}
      </div>
    </div>
    <div class="researcher-info">
      <h4>{{ person.name }}</h4>
      <p class="title">{{ person.title }}{% if person.supervisor %}<br><small>{{ person.supervisor }}</small>{% endif %}</p>
      <div class="social-links">
        {% if person.social.researchgate %}
          <a href="{{ person.social.researchgate }}" target="_blank" class="researchgate" title="ResearchGate" onclick="event.stopPropagation()">
            <i class="fab fa-researchgate"></i>
          </a>
        {% endif %}
        {% if person.social.linkedin %}
          <a href="{{ person.social.linkedin }}" target="_blank" class="linkedin" title="LinkedIn" onclick="event.stopPropagation()">
            <i class="fab fa-linkedin-in"></i>
          </a>
        {% endif %}
        {% if person.social.twitter %}
          <a href="{{ person.social.twitter }}" target="_blank" class="twitter" title="Twitter" onclick="event.stopPropagation()">
            <i class="fab fa-twitter"></i>
          </a>
        {% endif %}
        {% if person.social.website %}
          <a href="{{ person.social.website }}" target="_blank" class="website" title="Website" onclick="event.stopPropagation()">
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
      {% if person.keywords %}
      <div class="badges keywords">
        {% for keyword in person.keywords %}
          <span class="badge keyword-badge">{{ keyword }}</span>
        {% endfor %}
      </div>
      {% endif %}
      {% if person.locations %}
      <div class="badges locations">
        {% for location in person.locations %}
          <span class="badge location-badge">{{ location }}</span>
        {% endfor %}
      </div>
      {% endif %}
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
        {% if person.social.orcid %}
          <a href="{{ person.social.orcid }}" target="_blank" class="orcid">
            <i class="fab fa-orcid"></i> ORCID
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
      {% if person.keywords %}
      <div class="badges keywords">
        {% for keyword in person.keywords %}
          <span class="badge keyword-badge">{{ keyword }}</span>
        {% endfor %}
      </div>
      {% endif %}
      {% if person.locations %}
      <div class="badges locations">
        {% for location in person.locations %}
          <span class="badge location-badge">{{ location }}</span>
        {% endfor %}
      </div>
      {% endif %}
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
        {% if person.social.orcid %}
          <a href="{{ person.social.orcid }}" target="_blank" class="orcid">
            <i class="fab fa-orcid"></i> ORCID
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
      {% if person.keywords %}
      <div class="badges keywords">
        {% for keyword in person.keywords %}
          <span class="badge keyword-badge">{{ keyword }}</span>
        {% endfor %}
      </div>
      {% endif %}
      {% if person.locations %}
      <div class="badges locations">
        {% for location in person.locations %}
          <span class="badge location-badge">{{ location }}</span>
        {% endfor %}
      </div>
      {% endif %}
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
        {% if person.social.orcid %}
          <a href="{{ person.social.orcid }}" target="_blank" class="orcid">
            <i class="fab fa-orcid"></i> ORCID
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

<div class="section-title">
  <h3>Former PhD Students</h3>
  <div class="divider"></div>
</div>

<div style="max-width: 800px; margin: 0 auto 60px;">
  <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.8;">
    <li>Alison Prior (main supervisor: Colin Prentice)</li>
    <li>Neeraj Sah (2022) - Now at CEH, UK</li>
    <li>Will Veness (2023) - Research Consultant</li>
    <li>Anna Twomlow (2021)</li>
    <li>Charles Zogheib (2021)</li>
    <li>Simon De Stercke (2020)</li>
    <li>Hsi-Kai Chou (2020) - Next destination: University of Cardiff</li>
    <li>Boris Ochoa (2019) - Next destination: ATUK, Ecuador</li>
    <li>Peter Blair (2018) - Now at Thames Water, UK</li>
    <li>Sam Grainger (2018) - Now at University of Leeds, UK</li>
    <li>Tilashwork Chanie (2018)</li>
    <li>Xi Liu (2018)</li>
    <li>Jimmy O'Keeffe (2016)</li>
    <li>Bastian Manz (2016) - Now at Willis Re, UK</li>
    <li>Simon Moulds (2016) - Now at the University of Exeter, UK</li>
    <li>Claudia Vitolo (2015) - Now at ECMWF, Reading, UK</li>
    <li>Gina Tsarouchi (2015) - Now at HR Wallingford, UK</li>
    <li>Susana Almeida (2014) - Now at University of Bristol, UK</li>
    <li>Zed Zulkafli (2014) - Next destination: Universiti Putra Malaysia</li>
    <li>Emma Bergin (2013) - Next destination: Flood Re, London, UK</li>
  </ul>
</div>

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

