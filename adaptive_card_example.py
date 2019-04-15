# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Example content for an AdaptiveCard."""

ADAPTIVE_CARD_CONTENT =   [{
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "width": "3",
                "spacing": "none",
                "items": [
                  {
                    "type": "ColumnSet",
                    "columns": [
                      {
                        "type": "Column",
                        "width": "3",
                        "items": [
                          {
                            "type": "Image",
                            "width": "auto",
                            "url": "https://www.onedaykorea.com/wp-content/uploads/2014/11/one-day-korea-old-and-new-seoul-city-tour-gyeongbokgung-palace-changing-guards-ceremony-1.jpg"
                          }
                        ]
                      },
                      {
                        "type": "Column",
                        "width": "3",
                        "spacing": "medium",
                        "items": [
                          {
                            "type": "TextBlock",
                            "text": "Margie's Travel",
                            "weight": "bolder"
                          },
                          {
                            "type": "TextBlock",
                            "text": "4.4 stars",
                            "spacing": "none"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "TextBlock",
                    "text": "42 miles away",
                    "weight": "bolder"
                  },
                  {
                    "type": "TextBlock",
                    "text": "1602 E Avenue Rd.",
                    "spacing": "none"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Gig Harbor, WA 98335",
                    "spacing": "none"
                  }
                ]
              },
              {
                "type": "Column",
                "width": "1",
                "spacing": "none",
                "items": [
                  {
                    "type": "Image",
                    "url": "https://www.onedaykorea.com/wp-content/uploads/2015/03/one-day-korea-half-day-dmz-tour.jpg"
                  }
                ]

              }
            ]
          }

        ],
        "actions": [
          {
            "type": "Action.Submit",
            "title": "This one",
            "data": {
              "school": "Margie's Travel"
            }
          }
        ]
      }
    },
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "width": "3",
                "spacing": "none",
                "items": [
                  {
                    "type": "ColumnSet",
                    "columns": [
                      {
                        "type": "Column",
                        "width": "3",
                        "items": [
                          {
                            "type": "Image",
                            "width": "auto",
                            "url": "https://www.onedaykorea.com/wp-content/uploads/2018/06/Cheorwon-DMZ-and-Battle-Field-Day-Trip-from-Seoul.jpg"
                          }
                        ]
                      },
                      {
                        "type": "Column",
                        "width": "3",
                        "spacing": "medium",
                        "items": [
                          {
                            "type": "TextBlock",
                            "text": "Fabrikam",
                            "weight": "bolder"
                          },
                          {
                            "type": "TextBlock",
                            "text": "4.1 stars",
                            "spacing": "none"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "TextBlock",
                    "text": "13 miles away",
                    "weight": "bolder"
                  },
                  {
                    "type": "TextBlock",
                    "text": "217 W Pine St.",
                    "spacing": "none"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Seattle, WA 98126",
                    "spacing": "none"
                  }
                ]
              },
              {
                "type": "Column",
                "width": "1",
                "spacing": "none",
                "items": [
                  {
                    "type": "Image",
                    "url": "https://www.onedaykorea.com/wp-content/uploads/2017/11/goblin-the-lonely-and-great-god-shooting-location-tour.jpg"
                  }
                ]

              }
            ]
          }

        ],
        "actions": [
          {
            "type": "Action.Submit",
            "title": "This one",
            "data": {
              "school": "Fabrikam"
            }
          }
        ]
      }
    },
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "width": "3",
                "spacing": "none",
                "items": [
                  {
                    "type": "ColumnSet",
                    "columns": [
                      {
                        "type": "Column",
                        "width": "3",
                        "items": [
                          {
                            "type": "Image",
                            "width": "auto",
                            "url": "https://www.onedaykorea.com/wp-content/uploads/2017/11/goblin-the-lonely-and-great-god-shooting-location-tour.jpg"
                          }
                        ]
                      },
                      {
                        "type": "Column",
                        "width": "3",
                        "spacing": "medium",
                        "items": [
                          {
                            "type": "TextBlock",
                            "text": "Adventure Works",
                            "weight": "bolder"
                          },
                          {
                            "type": "TextBlock",
                            "text": "3.2 stars",
                            "spacing": "none"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "TextBlock",
                    "text": "7 miles away",
                    "weight": "bolder"
                  },
                  {
                    "type": "TextBlock",
                    "text": "510 N Yale Ave.",
                    "spacing": "none"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Seattle, WA 98127",
                    "spacing": "none"
                  }
                ]
              },
              {
                "type": "Column",
                "width": "1",
                "spacing": "none",
                "items": [
                  {
                    "type": "Image",
                    "url": "https://www.onedaykorea.com/wp-content/uploads/2017/11/goblin-the-lonely-and-great-god-shooting-location-tour.jpg"
                  }
                ]

              }
            ]
          }

        ],
        "actions": [
          {
            "type": "Action.Submit",
            "title": "This one",
            "data": {
              "school": "Adventure Works"
            }
          }
        ]
      }
    },
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "width": "3",
                "spacing": "none",
                "items": [
                  {
                    "type": "ColumnSet",
                    "columns": [
                      {
                        "type": "Column",
                        "width": "3",
                        "items": [
                          {
                            "type": "Image",
                            "width": "auto",
                            "url": "http://adaptivecards.io/content/Relecloud.png"
                          }
                        ]
                      },
                      {
                        "type": "Column",
                        "width": "3",
                        "spacing": "medium",
                        "items": [
                          {
                            "type": "TextBlock",
                            "text": "Relecloud Diving",
                            "weight": "bolder"
                          },
                          {
                            "type": "TextBlock",
                            "text": "4.7 stars",
                            "spacing": "none"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "TextBlock",
                    "text": "15 miles away",
                    "weight": "bolder"
                  },
                  {
                    "type": "TextBlock",
                    "text": "1210 W Hanford St.",
                    "spacing": "none"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Seattle, WA 98105",
                    "spacing": "none"
                  }
                ]
              }
            ]
          }

        ],
        "actions": [
          {
            "type": "Action.Submit",
            "title": "This one",
            "data": {
              "school": "Relecloud Diving"
            }
          }
        ]
      }
    }
]