package twitterscraper

import (
	"strconv"
	"context"
	"encoding/json"
	"testing"
)

func TestGetTweets(t *testing.T) {
	count := 0
	maxTweetsNbr := 50
	for tweet := range GetTweets(context.Background(), "Twitter", maxTweetsNbr) {
		if tweet.Error != nil {
			t.Error(tweet.Error)
		} else {
			count++

			jsonData, err := json.Marshal(&tweet)
			if err != nil { t.Error(err); }
			var jsonBlob = []byte(jsonData)
			var unmarshaled Tweet
			err = json.Unmarshal(jsonBlob, &unmarshaled)
			if err != nil { t.Error(err); }
			if _, err := strconv.Atoi(unmarshaled.ID); err != nil {
				t.Error("Expected unmarshaled.ID as a int not string\n")
			}

			if tweet.HTML == "" {
				t.Error("Expected tweet HTML is not empty")
			}
			if tweet.ID == "" {
				t.Error("Expected tweet ID is not empty")
			}
			// if tweet.UserID == "" {
			// 	t.Error("Expected tweet UserID is not empty")
			// }
			if tweet.Username == "" {
				t.Error("Expected tweet Username is not empty")
			}
			if tweet.PermanentURL == "" {
				t.Error("Expected tweet PermanentURL is not empty")
			}
			if tweet.Text == "" {
				t.Error("Expected tweet Text is not empty")
			}
			if tweet.TimeParsed.IsZero() {
				t.Error("Expected tweet TimeParsed is not zero")
			}
			if tweet.Timestamp == 0 {
				t.Error("Expected tweet Timestamp is greater than zero")
			}
		}
	}
	if count != maxTweetsNbr {
		t.Errorf("Expected tweets count=%v, got: %v", maxTweetsNbr, count)
	}
}
